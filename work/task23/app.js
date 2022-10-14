const express= require('express');
//for file system..files load..

const fs=require('fs');



//obj
app=express();

//handler...

app.get('/',function(request,response){

fs.readFile('index.html',function(err,data){
    //if file not exits..or ..file name not..
    if (err){
        throw err;
    }
    //if no error then file is in data...
    response.end(data)
})

})

//server..
app.listen(2000,function(){
    console.log('Server Started');
})
