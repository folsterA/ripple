export interface Server {
  description: string;
  id: string;
  name: string;
  profile_url: string;
}

export interface Channel {
  description: string;
  id: string;
  name: string;
  server_id: string;
  pinned_messages: string[];
}
