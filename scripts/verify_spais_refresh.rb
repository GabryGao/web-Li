#!/usr/bin/env ruby

require "yaml"

ROOT = File.expand_path("..", __dir__)

def load_yaml(path)
  YAML.safe_load(File.read(File.join(ROOT, path)), aliases: true)
end

def assert(condition, message)
  raise "CHECK FAILED: #{message}" unless condition
end

profile = load_yaml("_data/profile.yml")
pi = load_yaml("_data/pi.yml")
team = load_yaml("_data/team_members.yml")
publications = load_yaml("_data/publications.yml")

expected_students = {
  "Tengchao Yang" => nil,
  "Shunfa Zhao" => "Co-advised with Prof. Zhiwen Pan, University of Macau",
  "Jiahe Chen" => "Co-advised with Prof. Lansheng Han, Huazhong University of Science and Technology",
  "Di Xu" => "Co-advised with Prof. Lansheng Han, Huazhong University of Science and Technology",
  "Can Shen" => nil
}

assert(publications.length == 51, "expected 51 publications, found #{publications.length}")
assert(team.map { |member| member.fetch("name") } == expected_students.keys,
       "team names or order do not match the approved roster")

team.each do |member|
  assert(member["advising"] == expected_students.fetch(member.fetch("name")),
         "incorrect advising line for #{member.fetch("name")}")
end

assert(profile["career"].is_a?(Array) && !profile["career"].empty?,
       "profile.career must contain the third-person career summary")
assert(profile["about"].is_a?(Array) && !profile["about"].empty?,
       "profile.about must contain the restrained research summary")

visible_copy = [profile, pi].to_s
assert(!visible_copy.match?(/with honors|\(honors\)/i), "visible profile data still says honors")
assert(!visible_copy.match?(/\bI am\b|\bMy research\b/i), "profile data still uses first person")

header = File.read(File.join(ROOT, "_includes/header.html"))
home = File.read(File.join(ROOT, "_pages/home.html"))
about = File.read(File.join(ROOT, "_pages/about.html"))
openings_path = File.join(ROOT, "_pages/openings.html")
config = load_yaml("_config.yml")

assert(header.include?("spais-lab.png") && !header.include?("brand-mark"),
       "header must use the supplied SPAIS Lab logo instead of the XL mark")
assert(header.include?('class="brand-affiliation"') && header.include?("SPAIS Lab@PolyU"),
       "navbar must visibly identify the lab as SPAIS Lab@PolyU")
assert(config.fetch("nav_pages").any? { |item| item["name"] == "openings" },
       "Openings must be present in the primary navigation")
assert(home.include?("profile.career") && !home.include?("about-accent"),
       "Home must show career history and remove the duplicate XL About card")
assert(about.include?("profile.about") && !about.match?(/\bI am\b|\bMy research\b/),
       "About must render the restrained third-person research summary")
assert(about.include?("<h1>About</h1>") && !about.match?(/^## /),
       "About headings must render as HTML instead of visible Markdown markers")
assert(File.exist?(openings_path) && File.read(openings_path).include?("profile.recruiting"),
       "the dedicated Openings page must render verified recruiting data")

navbar_scss = File.read(File.join(ROOT, "_sass/components/_navbar.scss"))
team_scss = File.read(File.join(ROOT, "_sass/layouts/_team.scss"))
animation_scss = File.read(File.join(ROOT, "_sass/utilities/_animations.scss"))
assert(navbar_scss.include?(".brand-logo"), "navbar styles must size the wide SPAIS Lab logo")
assert(!team_scss.include?("max-width: 54rem"), "Team roster must use the available content width")
assert(!animation_scss.match?(/\.fade-in-section\s*\{[^}]*opacity:\s*0/m),
       "page content must remain visible when JavaScript or IntersectionObserver does not run")

puts "SPAIS refresh source checks passed (51 publications, 5 students)."
