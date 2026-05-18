-- Create user_progress table for normalized exam answer tracking
-- Replaces the JSON blob approach in kv_store_b9034bdd
-- 
-- To apply this migration, run via Supabase Dashboard SQL Editor or:
--   supabase migration new create_user_progress_table
--   (paste this SQL into the generated file)
--   supabase db push

create table if not exists user_progress (
    id uuid default gen_random_uuid() primary key,
    user_id uuid references auth.users(id) on delete cascade not null,
    exam_source text not null,
    exam_set_id integer not null,
    question_id integer not null,
    selected_answer integer not null,
    created_at timestamptz default now(),
    updated_at timestamptz default now(),
    unique(user_id, exam_source, exam_set_id, question_id)
);

-- Indexes for common query patterns
comment on table user_progress is 'Stores individual user answers per question. Replaces the old JSON blob kv_store approach.';

create index if not exists idx_user_progress_user_id 
    on user_progress(user_id);

create index if not exists idx_user_progress_user_source_set 
    on user_progress(user_id, exam_source, exam_set_id);

create index if not exists idx_user_progress_updated_at 
    on user_progress(updated_at);

-- Enable Row Level Security
alter table user_progress enable row level security;

-- RLS Policies: users can only access their own data

create policy "Users can view own progress"
    on user_progress for select
    using (auth.uid() = user_id);

create policy "Users can insert own progress"
    on user_progress for insert
    with check (auth.uid() = user_id);

create policy "Users can update own progress"
    on user_progress for update
    using (auth.uid() = user_id)
    with check (auth.uid() = user_id);

create policy "Users can delete own progress"
    on user_progress for delete
    using (auth.uid() = user_id);
