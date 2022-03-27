// Example data
const aob = 
[
    { framework: 'React.JS', website: 'Paypal' },
    { framework: 'React.JS', website: 'Tesla' },
    { framework: 'Angular', website: 'Google' },
    { framework: 'Vue.JS', website: 'Vue' },
    { framework: 'JavaScript', website: 'inblack67' },
]

const superobj=(aob,framework)=>{
    const obj={}
    aob.forEach((data)=>{
        if (data.hasOwnProperty(framework)){
            if(obj[data[framework]]){
              obj[data[framework]]++
            }else{
                obj[data[framework]]=1
            }
        }
    })
        let superArray=[]
        for(const i in obj){
            //superArray=[...superArray,{ framework:i ,count:obj[i]}]
            superArray.push({ framework:i ,count:obj[i]})

        }
        
    
    //console.log(obj)
console.log(superArray)
    
}

superobj(aob,"framework")