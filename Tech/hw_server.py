from typing import Callable

import asyncio

from myLogging import log
from framing import Frame


class HardwareServer:


    def __init__(self, newFrameCb: Callable[[str, Frame], None]) -> None:

        self.port = 8080
        
        self.newFrameCb = newFrameCb
        
        pass



    async def handler(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):

        addr = writer.get_extra_info("peername")

        log.info(f'HW | New connection from {addr}')

        try:
            # get hardware ID
            id = await reader.readuntil(b'\r')
            id = id[:-1].decode('utf-8')

            log.debug(f'HW | {addr} | Got id: {id}')

            while True:
                # wait for new frame
                frameStr = await reader.readuntil(b'\n')
                frameStr = frameStr.decode('utf-8')

                frame = Frame()
                
                # parse frame
                try:
                    frame.fromStr(frameStr)
                    log.info(f'HW | {addr} | ID: {id} | Received new frame')
                    await self.newFrameCb(id, frame)
                
                except Exception as e:
                    log.warning(f'HW | {addr} | ID: {id} | {str(e)}')


        except asyncio.IncompleteReadError:
            if reader.at_eof():
                log.info(f'HW | {addr} | Connection closed by hardware')

            else:
                log.warning(f'HW | {addr} | INCOMPLETE READ ERROR')

        
        log.info(f'HW | {addr} | Closing connection')

        writer.close()



    async def run(self) -> None:

        hw_server_sock = await asyncio.start_server(self.handler, "0.0.0.0", self.port)

        addr = hw_server_sock.sockets[0].getsockname()

        log.info(f'Hardware server started on {addr[0]}:{addr[1]}')

        async with hw_server_sock:
            await hw_server_sock.serve_forever()





if __name__ == "__main__":


    def newFrame(id: str, frame: Frame) -> None:

        log.info(f'Got new frame from id: {id} | frame.time: {frame.time} | frame.speed: {frame.speed}')

        pass

    server = HardwareServer(newFrameCb=newFrame)

    task = asyncio.get_event_loop().create_task(server.run())

    asyncio.get_event_loop().run_forever()
