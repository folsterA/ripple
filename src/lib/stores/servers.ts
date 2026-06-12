import { writable } from 'svelte/store';
import type { Server } from '$lib/types';

export const servers = writable<Server[]>([]);
