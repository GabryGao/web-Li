#!/usr/bin/env ruby

require "yaml"
require "pathname"

ROOT = Pathname.new(__dir__).join("..").expand_path
errors = []

publications_path = ROOT.join("_data/publications.yml")
publications = YAML.safe_load(
  publications_path.read,
  permitted_classes: [],
  aliases: false
)

unless publications.is_a?(Array)
  abort("#{publications_path}: expected a YAML array")
end

publications.each_with_index do |publication, index|
  label = "publication #{index + 1}"

  %w[title authors venue year].each do |key|
    errors << "#{label}: missing #{key}" if publication[key].to_s.strip.empty?
  end

  if publication["title"].to_s.match?(/\b(?:TDSC|TIFS)\s+20\d{2}\b/)
    errors << "#{label}: title contains venue/authors: #{publication['title']}"
  end

  %w[url website code dataset weights].each do |key|
    value = publication[key].to_s
    next if value.empty? || value.match?(%r{\Ahttps?://})

    errors << "#{label}: invalid #{key} URL #{value}"
  end
end

scan_paths = [
  ROOT.join("_config.yml").to_s,
  *Dir[ROOT.join("_pages/**/*").to_s],
  *Dir[ROOT.join("_data/**/*").to_s],
  *Dir[ROOT.join("_site/**/*.html").to_s]
].select { |path| File.file?(path) }

banned_patterns = [
  /Richard Feynman/i,
  /Caltech/i,
  /quantum electrodynamics/i
]

scan_paths.each do |path|
  text = File.read(path, encoding: "UTF-8")
  banned_patterns.each do |pattern|
    errors << "#{path}: contains #{pattern.inspect}" if text.match?(pattern)
  end
end

render_expectations = {
  "_site/index.html" => [
    "site-hero",
    "research-card",
    "news-link",
    "recruit-panel",
    "AI Security @ PolyU"
  ],
  "_site/publications/index.html" => [
    "publication-year",
    "publication-card"
  ],
  "_site/research/index.html" => [
    "agentic-ai-security",
    "responsible-ai",
    "trustworthy-ai-for-x"
  ]
}

render_expectations.each do |relative_path, markers|
  path = ROOT.join(relative_path)
  next unless path.file?

  html = path.read
  markers.each do |marker|
    errors << "#{relative_path}: missing rendered marker #{marker}" unless html.include?(marker)
  end
end

abort(errors.join("\n")) unless errors.empty?

puts "content verification passed"
