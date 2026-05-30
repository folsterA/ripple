<script lang="ts">
  import { invoke } from '@tauri-apps/api/core';
  import { onMount } from 'svelte';

  let { params } = $props();

  let channels = $state('');

  onMount(async () => {
    channels = await invoke('get_channels', { serverId: Number(params.server) });
  });
</script>

<h1>Server: {params.server}</h1>
<h1>Channels: {channels}</h1>
<p>This is the server homepage.</p>

<!-- this would be the default home page -->
