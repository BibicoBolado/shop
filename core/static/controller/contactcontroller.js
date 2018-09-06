class ContacController{
    constructor(){
        this.formEl   = document.getElementById('formContact');
        this.fileEl   = document.getElementById('file');
        this.choiceEl = document.getElementById('id_option');
        this.coiceValue;
        console.log("oi!");
        this.addEvent();
        this.fileEl.style.display = "none";
    }

    getValue(){
        return this.coiceValue = this.choiceEl.value;
    }

    addEvent(){
        this.choiceEl.addEventListener('change',()=>{
            let aux = this.getValue();
            if(aux=="6"){
                this.showFile();
            }else{
                this.hideFile();
            }
        });
    }

    showFile(){
        this.fileEl.style.display = "block";
    }
    hideFile(){
        this.fileEl.style.display = "none";
    }
}