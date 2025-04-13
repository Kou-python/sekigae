FROM ruby:3.2

WORKDIR /app

COPY Gemfile .
RUN bundle install

COPY main.rb .
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT ["/usr/bin/entrypoint.sh"]