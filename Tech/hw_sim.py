import asyncio
from datetime import datetime
import math

HOST = "localhost"
PORT = 8080

CAR_ID = "car1"

period = 16
alpha = (2.0 * math.pi) / period
dc_offset = 50.0
amplitude = 40.0

now = datetime.now


async def send_data():
    
    reader, writer = await asyncio.open_connection(HOST, PORT)

    print("Connected to server.")

    speed = math.sin(alpha * now().timestamp())

    speed = (speed * amplitude) + dc_offset

    frame = construct_frame(CAR_ID, now(), 0, 0, speed, 0, 0, 0, 0, False)

    print(f"Sending frame {frame.encode('utf8')}")

    writer.write(frame.encode("utf8"))

    writer.close()

    print("Closing connection with server")
    print()


def construct_frame(id: str, time: datetime, lng: float, lat: float, speed: float, rpm: int, temp: float, rt: int, fuel: float, check: bool) -> str:

    frame = id + '\r'
    frame += time.strftime("%d/%m/%Y_%M:%H:%S") + ' '
    frame += str(lng) + ' '
    frame += str(lat) + ' '
    frame += str(speed) + ' '
    frame += str(rpm) + ' '
    frame += str(temp) + ' '
    frame += str(rt) + ' '
    frame += str(fuel) + ' '
    if check:
        frame += '1'
    else:
        frame += '0'
    
    frame += '\n'

    return frame



async def simulate():
    while True:
        try:
            await send_data()
        
        except ConnectionRefusedError:
            print("Could not connect to server")
            print()

        await asyncio.sleep(1)


# task = asyncio.get_event_loop().create_task(simulate())

# asyncio.get_event_loop().run_forever()