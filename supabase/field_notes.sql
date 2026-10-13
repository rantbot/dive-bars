-- The field journal at the end of the film. Run this once in your Supabase project (SQL editor, New query, Run).
-- Viewers can add a note but can't read, change or delete anything. You read them in the Table editor.

create table if not exists public.field_notes (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  bar text not null check (char_length(bar) between 1 and 120),
  city text check (char_length(city) <= 120),
  protocol text check (char_length(protocol) <= 400),
  tip text check (char_length(tip) <= 600),
  name text check (char_length(name) <= 60)
);

alter table public.field_notes enable row level security;

drop policy if exists "Anyone can add a field note" on public.field_notes;
create policy "Anyone can add a field note" on public.field_notes
  for insert to anon with check (true);

-- No select, update or delete policies, so the public key can only add rows.
revoke select, update, delete on public.field_notes from anon;
grant insert on public.field_notes to anon;
