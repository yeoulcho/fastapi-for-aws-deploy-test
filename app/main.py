# This is a sample Python script.
from typing import Optional

from fastapi import FastAPI


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #python_basics()
    #functions_test()
    # gas_station_problem_solve()
    # class_test_function()
    # AccessControlTest()

    #thread_test_sequence()
    # perform_add_process()
    #perform_add_process_lock()
    print("hi")

app = FastAPI()

@app.get("/")
async def root_index():
    return {"message": "Hello from FASTAPI AWS"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


origins = ["http://localhost:8080"]
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # *별 찍으면 안됨! 전부다 허용하겠다는 이야기라
    allow_credentials=True,
    allow_methods=["*"], # *은 전부다
    allow_headers=["*"],
)

