<template>
   <Card>
        <div class="flex justify-between text-center">
            <span class="text-[#1C3B4F] font-bold text-[20px]">Trending topics</span>
            <img src="~/assets/images/trend.svg" alt="Nature" />
        </div>
        <div class="flex flex-wrap justify-start items-center p-0">
            <span v-for="(topic,index) in trending" :key="topic+index" class="text-native bg-white px-4 py-2 m-2 rounded-full"
                @click="selectTopic(topic)"
            >
                {{ topic }}
            </span>
        </div>
    </Card>
</template>

<script setup lang="ts">
    const { trending, selectTopic } = useTopics()

</script>

<style scoped>

</style>