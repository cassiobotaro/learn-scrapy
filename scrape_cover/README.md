# Scrape cover

Proof of concept to demonstrate how to download images using the image pipeline.

## Steps

**Step 1:**

Add these lines into `settings.py`

```python
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}
IMAGES_STORE = './'
```

**Step 2:**

The returned item must contain the value "image_urls" and its value will be a list of images to be retrieved.

```python
        # ...
        yield {"image_urls": [
            response.urljoin(cover_url),
            ]}
```
