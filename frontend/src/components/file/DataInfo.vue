<template>
  <div class="container mx-auto p-10">
    <p class="text-xl">2)Details</p>
    <div
      class="
        bg-green-500
        h-12
        rounded-xl
        flex
        content-center
        items-center
        pl-10
      "
    >
      <p class="text-white">
        <b>{{rowSize}} rows</b> ({{totalSize}} cells) are parsed from the file
      </p>
    </div>

    <div class="h-60 w-auto border-4 container bg-green-100 p-4 mt-5 rounded">
      <h3 class="text-xl">Columns</h3>
      <div class="h-40 p-5">
        <div class="flex flex-wrap ">
          <div class="col-card flex justify-between" v-for="(col,index) in cols" :key="col">
            <p><b class="">{{cols[index]}}</b></p><p> {{dtypes[index]}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DataInfo",
  props:["cols","dtypes","rowSize","totalSize"],
};
</script>

<style >
.col-card {
  @apply bg-green-500 w-48 rounded-lg text-white p-1 pl-3 pr-3 m-2;
}
</style>