class IndexController{

    constructor(){
        this.aux =0;
        this.bodyEl = document.getElementById('my-body');
        this.mouseLeaveBody();
    }

    mouseLeaveBody(){
        this.bodyEl.addEventListener('mouseleave',()=>{
            if(this.aux==0){
                alert("Funcionou!");
                this.aux=1;
            }else{
                this.aux+=1;
                //console.log(this.aux);
            }    
        });
    }

}