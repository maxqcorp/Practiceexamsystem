import { createClient, SupabaseClient } from '@supabase/supabase-js';
import { projectId, publicAnonKey } from './info';

const supabaseUrl = `https://${projectId}.supabase.co`;

// Use global singleton pattern to prevent multiple instances across HMR
declare global {
  // eslint-disable-next-line no-var
  var __supabase: SupabaseClient | undefined;
}

export const supabase = globalThis.__supabase ?? (() => {
  const client = createClient(supabaseUrl, publicAnonKey, {
    auth: {
      persistSession: true,
      storageKey: 'sb-cpiuesklcoawoatbcflh-auth-token',
    },
  });
  globalThis.__supabase = client;
  return client;
})();
