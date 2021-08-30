<template>
  <div>
    <input name="file" type="file" @change="upload" />
    <button @click="onUpload">Upload</button>
    <p v-if="selectedFile"><b>File selected (now click upload)</b></p>

    <div class="xyplot">
      <br />
      <label>X axis (String) :    </label>
      <select v-model="x">
        <option v-for="col in columns" :key="col">{{ col }}</option>
      </select>
      <br />
      <br />
      <label>Y axis (number) :   </label>
      <select v-model="y">
        <option v-for="col in columns" :key="col">{{ col }}</option>
      </select>
    </div>
    <br>
  <div>
    <button @click="onClear">Clear selection</button>
  </div>
    <div v-if="x && y" class="plotted">
      x and y done
      <p>{{datam[x]}}</p>
      <p>{{datam[y]}} </p>
     <HelloWorld :xax="datam[x]" :yax="datam[y]" :key="x[0]"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import HelloWorld from "./components/HelloWorld.vue";
export default {
  name: "App",
  components: { HelloWorld },
  data() {
    return {
      selectedFile: null,
      datam: null,
      columns: null,
      selec: null,
      x: null,
      y: null,
      
    };
  },
  methods: {
    onClear(){
      this.x=null;
      this.y=null;
    },
    upload(event) {
      this.selectedFile = event.target.files[0];
    },
    onUpload() {
      const formData = new FormData();
      formData.append("file", this.selectedFile, this.selectedFile.name);
      axios
        .post(
          "https://CloudyPuzzledDominspector.abisnhss.repl.co/upload",
          formData
        )
        .then((response) => {
          this.columns = response.data.columns;
          this.datam = response.data;
          console.log(this.datam);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
