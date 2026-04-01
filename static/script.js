function order(item){

fetch("/order",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({item:item})
})

.then(res=>res.json())
.then(data=>alert(data.message))

}