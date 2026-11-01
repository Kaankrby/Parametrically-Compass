"""Real subprocess MCP handshake, resources and read-only tool calls."""
import asyncio
import json
from pathlib import Path
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    root = Path(__file__).resolve().parents[1]
    params = StdioServerParameters(command=sys.executable, args=[str(root / 'mcp_server/server.py')])
    async with stdio_client(params) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            tools = (await session.list_tools()).tools
            assert len(tools) == 5
            assert all(t.annotations.readOnlyHint and not t.annotations.destructiveHint for t in tools)
            cases = [('compass_source_status', {}), ('compass_list_documents', {}),
                     ('compass_read_document', {'document_id': 'yonetmelik', 'max_lines': 30}),
                     ('compass_search', {'query': 'proje kodu', 'limit': 3}),
                     ('compass_read_table', {'table_id': 'p001-t01', 'limit': 2})]
            for name, arguments in cases:
                result = await session.call_tool(name, arguments)
                assert not result.isError, result
                data = result.structuredContent
                if data is None:
                    data = json.loads(result.content[0].text)
                assert data, name
                print('PASS:', name)
            rejected = await session.call_tool('compass_read_document', {'document_id': '../LICENSE'})
            assert rejected.isError
            status = await session.read_resource('compass://status')
            assert 'OCR_UNREVIEWED' in status.contents[0].text
            document = await session.read_resource('compass://documents/yonetmelik')
            assert 'MADDE 1' in document.contents[0].text
            assert len((await session.list_resource_templates()).resourceTemplates) == 1
            print('PASS: real stdio MCP, 5 tools, resources and invalid-path rejection')


if __name__ == '__main__':
    asyncio.run(main())
