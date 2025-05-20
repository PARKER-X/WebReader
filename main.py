import os
import asyncio
from pydantic_ai import Agent # type: ignore
from pydantic_ai.mcp import MCPServerStdio # type: ignore
from dotenv import load_dotenv

mcp_fetch_server = MCPServerStdio(
    command="python",
    args=["-m","mcp_server_fetch"]
)


agent = Agent(
    model = "groq:\\llama-3.3-70b-versatile",
    mcp_servers = [mcp_fetch_server]
)

async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("extract the content and summarize it: https://jalammar.github.io/illustrated-transformer/ ")
        output = result.output
        return output


if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)
    
