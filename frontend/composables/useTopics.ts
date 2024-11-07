

export function useTopics() {
    const error = useState('error', () => ref(''));
    const loading = useState('loading', () => ref(false));
    const query = useState('query', () => ref(''));
    const data = ref([]);
    const trending = useState('trending', () => ref(['data science', 'biology', 'ai', 'longevity', 'trading']))
    const searchOptions = useState('searchOptions', () => ref<any>([]))
    const selectedTopic = useState('selectedTopic', () => ref(trending.value[0]));
    const topChannels = useState('topChannels', () => ref([
        {
            topic: 'Ai in chiang mai',
            mentions: 536
        },
        {
            topic: 'Data Scientists',
            mentions: 125
        },
        {
            topic: 'Shill your session',
            mentions: 36
        }
    ]));


    const selectTopic = (topic: string) => {
        selectedTopic.value = topic;
    }

    const submitQuery = async () => {
        loading.value = true;
        try {
            await new Promise(resolve => setTimeout(resolve, 3000));
            searchOptions.value = trending.value.filter((topic: string) =>
                topic.toLowerCase().includes(query.value?.toLowerCase()?.trim() || "")
            );
        } catch (e: any) {
            error.value = e;
        } finally {
            if(searchOptions.value.length === 0) {
                error.value = 'No relevant topics are discussed on this server';
            } else error.value = '';

            loading.value = false;
        }
    }
    
    return { 
        loading, 
        error, 
        data, 

        query,
        trending, 
        selectedTopic, 
        topChannels,
        searchOptions,
        selectTopic,
        submitQuery
    };
}