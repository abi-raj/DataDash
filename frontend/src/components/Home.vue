<template>
    <div>

<NavBar />
<LoadFile/>
    </div>
</template>

<script>
import NavBar from './navbar/NavBar.vue';
import LoadFile from './file/LoadFile.vue';
    export default {
        name:"Home",
        components:{
            NavBar,
            LoadFile
        }
    }
</script>

<style  scoped>

</style>