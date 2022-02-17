
const socket = new WebSocket("ws://localhost:8080")


socket.onmessage =  ({data})=>{
    console.log("message sent!",data)
}

document.querySelector(".btnsend").addEventListener("click",function(){
    socket.send("hello")
})