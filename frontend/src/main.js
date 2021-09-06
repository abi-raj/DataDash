import { createApp } from 'vue'
import {
    createStore
} from "vuex";

// import App from './App.vue'

import Home from './components/Home.vue'

import './assets/tailwind.css'


const store = createStore({
state(){
    return {
        fileSelected:null,
        fileData: {
            allData: null,
            columns: null,
            dtypes: null,
            rowSize: null,
            totalSize: null,
          },
          picked:null,
    }
},
mutations:{
    setFileSelected(state,file){
        state.fileSelected = file
        
    },
    setFileData(state,data){
    
        state.fileData.columns = data.columns;
     
        state.fileData.allData = data;
        state.fileData.dtypes = data.dtypes;
        state.fileData.rowSize = data.rowSize;
        state.fileData.totalSize = data.totalSize;
    },
    setDisplayType(state,data){
        state.picked = data
    } ,

},
getters:{
stringColumns:(state)=>{
let result=[];
    for(let i=0;i<state.fileData.columns.length;i++){
    if(state.fileData.dtypes[i]==="String"){
        result.push(state.fileData.columns[i])
    }
    }
return result
},
numberColumns:(state)=>{
    let result=[];
    for(let i=0;i<state.fileData.columns.length;i++){
    if(state.fileData.dtypes[i]==="Number"){
        result.push(state.fileData.columns[i])
    }
    }
return result
}
}
})

const app=createApp(Home);
app.use(store);
app.mount('#app')
