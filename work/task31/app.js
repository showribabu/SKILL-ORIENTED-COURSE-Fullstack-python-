const express=require('express')

var app=express()

app.get('/',function(req,res){
    res.send('Showri');
})

app.listen(2300,function(){
    console.log('server strat')
})