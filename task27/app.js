const express=require('express')
const mysql=require('mysql2')

//obj..
var app=express()
var conn=mysql.createConnection({

    host:'localhost',
    user:'root',
    password:'kits',
    database:'showri'
});

//handlers..direct from url...

app.get('/data',function(req,res){

    conn.connect(function(err){
        if(err){
            throw err;
        }
        var sql="select * from book";
        conn.query(sql,function(err,result){
            if(err){
                throw err;
            }
            var data=[]
            for(let i of result){
                data.push(JSON.stringify(i))
            }
            res.end(data.toString());
        })

        
    })
})

//server..

app.listen(2000,function(){
    console.log('Server Started');
})