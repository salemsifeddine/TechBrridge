


var datas=""


socket.onmessage =  ({data})=>{
    // const d = new Date();
    // let minutes = d.getSeconds();
    appendarraygraph.push(data)
    // randomsec.push(minutes)
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


document.querySelector(".rangetime").addEventListener("click",function(){
    var rangetime=document.querySelector("#selcrng").value
    socket.close();
    
    setTimeout(() => {
        var socket1=new WebSocket("ws://localhost:8081");
    
   
    appendarraygraph=[]
     socket1.onopen =  ()=>{
   
        var datasend=`car1,client1,${rangetime}`
    
        JSON.stringify(datasend)
    
         socket1.send(datasend)
        document.querySelector(".chart-container-header span").textContent = rangetime
    }
     socket1.onmessage =  ({data})=>{
        appendarraygraph.push(data)
        // document.write([data])
        // appendarraygraph.append(parseInt(data))
        console.log(appendarraygraph)
        
    }
    }, 3000);
})

