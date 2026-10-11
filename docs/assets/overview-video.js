(() => {
  const video = document.getElementById('overview-video');
  const button = document.querySelector('.video-play');
  if (!video || !button) return;
  const label = button.querySelector('span');
  const sync = () => {
    const playing = !video.paused && !video.ended;
    button.classList.toggle('is-playing', playing);
    label.textContent = playing ? 'Pause video' : 'Play video';
    button.setAttribute('aria-label', playing ? 'Pause overview video' : 'Play overview video');
  };
  const play = () => video.play().catch(sync);
  button.hidden = false;
  button.addEventListener('click', () => {
    if (!video.paused) return video.pause();
    play();
    if (window.matchMedia('(max-width: 800px)').matches) {
      video.scrollIntoView({behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center'});
    }
  });
  ['play', 'pause', 'ended', 'error'].forEach(event => video.addEventListener(event, sync));
  sync();
})();
