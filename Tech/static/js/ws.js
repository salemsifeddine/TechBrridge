
const socket = new WebSocket("ws://localhost:8080")

var datas=""
socket.onmessage =  ({data})=>{
    document.write(data)
    datas=data
}

document.querySelector(".btnsend").addEventListener("click",function(){
    socket.send("hello")
    document.write(datas)
})