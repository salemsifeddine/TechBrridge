
const socket = new WebSocket("ws://localhost:8080")


socket.onmessage =  ({data})=>{
    document.write(data)
}

document.querySelector(".btnsend").addEventListener("click",function(){
    socket.send("hello")
    document.write("data")
})