<template>
  <div>
    
    <input name="file" type="file" @change="upload" />
    <button @click="onUpload">Upload</button>
    <p v-if="selectedFile">selected</p>
    <div v-if="columns">
      <l>Columns:</l
      ><select v-model="selected" name="colum">
        <option v-for="col in columns" :key="col">{{ col }}</option>
      </select>
    </div>
<p>{{selected}}</p>
    <div v-if="selected">
      <ul>
        <li :for="val in data.selected">{{ val }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",

  data() {
    return {
      selectedFile: null,
      data: null,
      columns: null,
      selected: '',
    };
  },
  methods: {
    upload(event) {
      this.selectedFile = event.target.files[0];
    },
    onUpload() {
      const formData = new FormData();
      formData.append("file", this.selectedFile, this.selectedFile.name);
      axios
        .post(" https://0e13-103-163-248-199.ngrok.io/upload", formData)
        .then((response) => {
          console.log(response.data)
          this.columns = response.data.columns;
          console.log(response.data.columns);
          // console.log(response.data.columns)
          //"https://kurius.herokuapp.com/upload"
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
