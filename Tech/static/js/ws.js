
const socket = new WebSocket("ws://localhost:8081")

var datas=""


socket.onmessage =  ({data})=>{
    document.write(data)
    
}
socket.onerror =  ({data})=>{
    document.write(data)
    
}

socket.onopen =  ()=>{
   
    var datasend=`234,122`

    JSON.stringify(datasend)

    socket.send(datasend)
}


document.querySelector(".btnsend").addEventListener("click",function(){
    socket.send("hello")
    // document.write(datas)
})