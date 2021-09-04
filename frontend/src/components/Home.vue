<template>
    <div>

<NavBar />
<LoadFile/>
<DataInfo v-if="yes"/>
    </div>
</template>

<script>
import NavBar from './navbar/NavBar.vue';
import LoadFile from './file/LoadFile.vue';
import DataInfo from './file/DataInfo.vue'
    export default {
        name:"Home",
        data() {
            
            return {  
                yes:false,
            }      },
        components:{
            NavBar,
            LoadFile,
            DataInfo,
        }
    }
</script>

<style  scoped>

</style>