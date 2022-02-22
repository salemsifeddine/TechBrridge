
const socket = new WebSocket("ws://localhost:8081")

var datas=""


socket.onmessage =  ({data})=>{
    appendarraygraph.push(data)
    // document.write([data])
    // appendarraygraph.append(parseInt(data))
    console.log(appendarraygraph)
    
}
socket.onerror =  ({data})=>{
    // document.write(data)
    
}

socket.onopen =  ()=>{
   
    var datasend=`car1,client1`

    JSON.stringify(datasend)

    socket.send(datasend)
}


