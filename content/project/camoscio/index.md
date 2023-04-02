---
title: Camoscio
summary: An Italian instruction-tuned LLaMA

tags:
- opensource

date: "2023-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: "https://github.com/teelinsan/camoscio"

image:
  # caption: Photo by rawpixel on Unsplash
  focal_point: Smart


# url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

authors:
  - santilli

---

<div class="col-12 col-lg-8">

  <div class="mb-3">
    <form name="contact" method="POST" {{ $post_action | safeHTMLAttr }} {{ if $use_netlify_form }}netlify-honeypot="_gotcha"{{ end }} {{ if $use_netlify_captcha }}data-netlify-recaptcha="true"{{ end }} {{ with $block.Params.content.form.netlify.success_url }}action="{{ . | relLangURL }}"{{ end }}>
    <!-- <form name="contact" method="POST" action="mailto:donatocrisostomi@gmail.com">  -->
      <div class="form-group form-inline">
        <label class="sr-only" for="inputName"></label>
        <input type="text" name="name" class="form-control w-100" id="inputName" placeholder="Name" required>
      </div>
      <div class="form-group form-inline">
        <label class="sr-only" for="inputEmail"></label>
        <input type="email" name="email" class="form-control w-100" id="inputEmail" placeholder="Email" required>
      </div>
      <div class="form-group">
        <label class="sr-only" for="inputMessage"></label>
        <textarea name="message" class="form-control" id="inputMessage" rows="5" placeholder="Message" required></textarea>
      </div>
    <button type="submit" class="btn btn-primary px-3 py-2 w-100">"Send"</button>
    </form>
  </div>

</div> 