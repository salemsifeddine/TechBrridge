
const socket = new WebSocket("ws://localhost:8081")

var datas=""


socket.onmessage =  ({data})=>{
    document.write(data)
    
}
socket.onerror =  ({data})=>{
    document.write(data)
    
}

socket.onopen =  ()=>{
    var obj={}
    obj["ClientId"]="ClientId"
    obj["CarId"]="CarId"
    var datasend=`carId:carid,clientId:clientId`

    JSON.stringify(datasend)

    socket.send(datasend)
}


document.querySelector(".btnsend").addEventListener("click",function(){
    socket.send("hello")
    // document.write(datas)
})