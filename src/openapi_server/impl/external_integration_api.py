# coding: utf-8

from fastapi import FastAPI

from bert.concord import concord
from bert.model_manager import ModelManager
from bert.pre_process import extract_text_segments
from concord.server.models.memory_request import MemoryRequest
from concord.server.models.plugin_response import PluginResponse
from concord.server.models.setup_complete200_response import SetupComplete200Response

app = FastAPI()


async def process_memory(memory_request: MemoryRequest) -> PluginResponse:
    topic_model = ModelManager.get_model()
    messages = extract_text_segments(memory_request.transcript_segments)
    processed_count, error = concord(topic_model, messages)
    # TODO implement search DB for related channels
    if processed_count == 0:
        return PluginResponse(
            plugin_name="Concord",
            result="No topics found in the messages.",
            status="success",
        )
    if error is not None:
        return PluginResponse(
            plugin_name="Concord",
            result="Error processing messages: " + error,
            status="failure",
            error=error,
        )
    return PluginResponse(
        plugin_name="Concord",
        # TODO: implement related channels
        result="Processed " + str(processed_count) + " messages.",
        status="success",
    )


async def setup_complete():
    return SetupComplete200Response()
