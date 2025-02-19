"""
Application entrypoint
"""
import logging
from livekit.plugins import silero
from livekit.agents.pipeline import VoicePipelineAgent
from livekit_playground.agent.options import create_worker_options
from livekit_playground.agent.context import create_initial_context
from livekit_playground.speech_to_text.deepgram import deepgram_stt
from livekit_playground.text_to_speech.eleven_labs import eleven_labs_tts
from livekit_playground.large_language_models.anthropic import anthropic_claude_llm
from livekit.agents import AutoSubscribe, JobContext, JobProcess,cli,metrics


def prewarm(proc: JobProcess):
    """
    Load Silero weights and store to process userdata
    """
    proc.userdata["vad"] = silero.VAD.load()

async def entrypoint(ctx: JobContext):
    initial_ctx = create_initial_context()

    logging.info(f"connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for the first participant to connect
    participant = await ctx.wait_for_participant()
    logging.info(f"starting voice assistant for participant {participant.identity}")

    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=deepgram_stt,
        llm=anthropic_claude_llm,
        tts=eleven_labs_tts,
        min_endpointing_delay=0.5,
        max_endpointing_delay=5.0,
        chat_ctx=initial_ctx,
    )

    usage_collector = metrics.UsageCollector()

    @agent.on("metrics_collected")
    def on_metrics_collected(agent_metrics: metrics.AgentMetrics):
        metrics.log_metrics(agent_metrics)
        usage_collector.collect(agent_metrics)

    agent.start(ctx.room, participant)

    # Initial greeting
    await agent.say("Здравейте, аз съм Елена от Остеостронг. Как сте?", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(create_worker_options(prewarm, entrypoint))
