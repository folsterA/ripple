<script lang="ts">
  import { onMount } from 'svelte';
  import { openUrl } from '@tauri-apps/plugin-opener';

  onMount(() => {
    const handler = (event: MouseEvent) => {
      const target = event.target as HTMLElement | null;
      if (!target) return;

      // find external links
      const anchor = target.closest<HTMLAnchorElement>('a[rel="external"]');
      if (!anchor) return;

      const href = anchor.getAttribute('href');
      if (!href) return;

      event.preventDefault();
      openUrl(href);
    };

    document.addEventListener('click', handler);
    return () => document.removeEventListener('click', handler);
  });
</script>
