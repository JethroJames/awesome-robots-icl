// Leave native controls available if scripting or autoplay is unavailable.
(() => {
  const video = document.getElementById('research-video');
  if (!video) return;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let attempted = false;
  video.muted = true;
  const observer = new IntersectionObserver(entries => {
    if (!attempted && entries.some(entry => entry.isIntersecting)) {
      attempted = true;
      observer.disconnect();
      if (!reducedMotion.matches) video.play().catch(() => {});
    }
  }, { threshold: 0.3 });
  observer.observe(video);
  reducedMotion.addEventListener('change', event => {
    if (event.matches) video.pause();
  });
  // Follow the footage-credit link to its content, including with a direct hash.
  const revealCredits = () => {
    if (window.location.hash === '#footage-credits') {
      document.querySelector('#footage-credits details').open = true;
    }
  };
  window.addEventListener('hashchange', revealCredits);
  revealCredits();
})();
