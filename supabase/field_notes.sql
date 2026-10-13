-- The field journal at the end of the film, and the bathroom wall that shows it.
-- Run this in your Supabase project (SQL editor, New query, Run). It's safe to run again.
-- Viewers can add a note and read notes that aren't hidden. They can't change or delete anything.
-- To take a note off the wall, open the Table editor and tick "hidden" on that row.

create table if not exists public.field_notes (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  bar text not null check (char_length(bar) between 1 and 120),
  city text check (char_length(city) <= 120),
  protocol text check (char_length(protocol) <= 400),
  tip text check (char_length(tip) <= 600),
  name text check (char_length(name) <= 60)
);
alter table public.field_notes add column if not exists hidden boolean not null default false;

alter table public.field_notes enable row level security;

drop policy if exists "Anyone can add a field note" on public.field_notes;
create policy "Anyone can add a field note" on public.field_notes
  for insert to anon with check (hidden = false);

drop policy if exists "Anyone can read the wall" on public.field_notes;
create policy "Anyone can read the wall" on public.field_notes
  for select to anon using (hidden = false);

-- The public key can add the note fields and read them back. Nothing else.
revoke all on public.field_notes from anon;
grant insert (bar, city, protocol, tip, name) on public.field_notes to anon;
grant select (id, created_at, bar, city, protocol, tip, name, hidden) on public.field_notes to anon;
