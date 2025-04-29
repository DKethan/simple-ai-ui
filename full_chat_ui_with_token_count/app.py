from UI4AI import run_chat
from Wrapper4AI.wrap import connect

client = connect("openai", "gpt-40", "your-api-key")

run_chat(
    generate_response=client.chat_with_history,
    generate_title=client.generate_title,
    count_tokens=client.count_tokens,
)

