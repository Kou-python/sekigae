require 'thor'
require 'slack-notifier'

WEBHOOK_URL = "https://hooks.slack.com/services/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"
MEMBER      = %w[青木 伊藤 唐澤 川崎 小林 迫 笹川 塩澤 玉井]

class Sekigae < Thor
  desc "seat_change", "Send the results of the seat change to Slack"
  def seat_change
    shuffled_members = MEMBER.shuffle
    seats            = Array.new(5) { Array.new(2, "　") }
    seats[0][1]      = "固定"
    member_index     = 0

    seats.each_with_index do |row, i|
      row.each_with_index do |_, j|
        next if i == 0 && j == 1
        seats[i][j] = shuffled_members[member_index]
        member_index += 1
      end
    end

    seat_layout = "```\n"
    seat_layout += "席替え結果:\n"
    seat_layout += "┌───────┬───────┐\n"
    seats.each_with_index do |row, i|
      row.each do |name|
        seat_layout += "│ #{name.center(4)} "
      end
      seat_layout += "│\n"
      seat_layout += "├───────┼───────┤\n" unless i == seats.size - 1
    end
    seat_layout += "└───────┴───────┘"
    seat_layout += "```"

    notifier = Slack::Notifier.new(WEBHOOK_URL)
    notifier.ping(seat_layout)
    puts "finished"
  end
end

Sekigae.start(ARGV)