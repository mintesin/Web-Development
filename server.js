// EJS-Embedde javascript 
const express=require('express')
const bodyparser=require('body-parser')
const date=require(__dirname+'/data.js')
const items=[]

app=express()
app.set('view engine','ejs')
app.use(bodyparser.urlencoded({extended:true}))
app.use("/",express.static('public'))

app.get('/',function(req,res){
    
    const day=date.getDate();
    // res.write("<h1>Hello there the day is" + day+"</h1>" )
    // res.write("<h1>hello you have to come to work</h1>")
    res.render('list',{tday:day , NewItem:items})
})
app.post('/',function(req,res){
    const item=String(req.body.Newitem)
    items.push(item)
    res.redirect('/')
})

app.listen(3000,function(){
    console.log("Already Started........")
})