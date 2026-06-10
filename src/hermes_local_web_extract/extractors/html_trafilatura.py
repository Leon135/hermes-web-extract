"""Primary HTML extractor using trafilatura."""

import logging

import trafilatura
import trafilatura.settings
from trafilatura.metadata import extract_metadata

from hermes_local_web_extract.extractors.base import ExtractionResult

logger = logging.getLogger(__name__)


class TrafilaturaExtractor:
    def extract(self, content: bytes, url: str, content_type: str) -> ExtractionResult:
        result = ExtractionResult(extractor_name="trafilatura")

        try:
            html_str = content.decode("utf-8", errors="replace")
        except Exception as exc:
            result.warnings.append(f"Failed to decode HTML: {exc}")
            return result

        try:
            # Extract main content as text
            text = trafilatura.extract(
                html_str,
                url=url,
                include_comments=False,
                include_tables=True,
                no_fallback=False,
                favor_precision=False,
            )

            # Extract with markdown output
            markdown = trafilatura.extract(
                html_str,
                url=url,
                include_comments=False,
                include_tables=True,
                no_fallback=False,
                favor_precision=False,
                output_format="markdown",
            )

            result.text = text
            result.markdown = markdown or text

            if not text and not markdown:
                result.warnings.append("trafilatura returned empty content.")
        except Exception as exc:
            logger.debug("trafilatura extraction error: %s", exc)
            result.warnings.append(f"trafilatura extraction error: {exc}")

        # Extract metadata separately
        try:
            meta = extract_metadata(html_str, default_url=url)
            if meta:
                result.title = meta.title
                result.author = meta.author
                result.date = meta.date
                result.sitename = meta.sitename if hasattr(meta, "sitename") else None
        except Exception as exc:
            logger.debug("trafilatura metadata error: %s", exc)

        return result
