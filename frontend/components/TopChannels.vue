<template>
    <Card>
        <div class="flex flex-col gap-5 justify-between text-center">
            <span class="text-[#1C3B4F] font-bold text-[20px]">{{ props.title }}</span>
            <div class="flex">
                <span v-if="props.selectedTopic" class="text-white bg-[#2794BF] px-4 py-2 mt-4 rounded-full justify-self-start">
                    {{ props.selectedTopic }}
                </span>
            </div>
            <div
                class="flex flex-col gap-3"
            >
                <span v-for="(channel,index) in props.topChannels" :key="channel.topic+index">
                    <Tile>
                        <template #topic>
                            {{ channel.topic }}
                        </template>
                        <template #mentions>
                            {{ channel.mentions }} mentions
                        </template>
                    </Tile>
                </span>
                <div class="flex justify-center items-center gap-1 px-4 py-2 text-base bg-[#F4F4F4] rounded-2xl text-left">
                    <span>Show more </span>
                    <img src="~/assets/images/caret-down.svg" alt="">
                </div>
            </div>
        </div>
    </Card>
</template>

<script setup lang="ts">
    const props = defineProps(['title', 'selectedTopic', 'topChannels'])
</script>

<style scoped>

</style>