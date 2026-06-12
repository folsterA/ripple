<script lang="ts">
  import { resolve } from '$app/paths';
  import type { Channel } from '$lib/types.js';
  import { invoke } from '@tauri-apps/api/core';
  import { onMount } from 'svelte';

  let { children, params } = $props();
  let channels: Channel[] = $state([]);
  let serverId: string = $state('');

  onMount(async () => {
    serverId = params.server;

    channels = await invoke<Channel[]>('get_channels', { serverId }).catch((e) => {
      console.error('get_channels failed', e);
      return [];
    });
  });
</script>

<div class="flex h-full pr-1 bg-gray-700">
  <aside class="flex flex-col bg-gray-500 space-y-2 p-2">
    <nav>
      <ul>
        {#each channels as channel (channel.id)}
          <li><a href={resolve(`/${serverId}/${channel.id}`)}>channel: {channel.name}</a></li>
        {/each}
      </ul>
    </nav>
  </aside>
  <div class="flex-1 pl-3 bg-gray-700 overflow-auto custom-scrollbar">
    {@render children()}
  </div>
</div>
