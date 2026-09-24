const duration = name => {
  const fallback = {fast:160, base:240, disclosure:280, reveal:380, scroll:480};
  const value = getComputedStyle(document.documentElement).getPropertyValue(`--motion-${name}`).trim();
  const parsed = parseFloat(value) * (value.endsWith('ms') ? 1 : 1000);
  return Number.isFinite(parsed) && parsed > 0 ? parsed : fallback[name];
};
const easing = 'cubic-bezier(.22,1,.36,1)';
const nav = document.querySelector('.nav');
const navLinks = [...nav.querySelectorAll('a')];
const track = nav.querySelector('.nav-track');
let scrollAnimation = null;
let scrollQueued = false;
let activeId = '';
function markActive(id) {
  const active = navLinks.find(link => link.hash === '#' + id);
  if (!active) return;
  if (activeId !== id) {
    navLinks.forEach(link => link === active ? link.setAttribute('aria-current', 'location') : link.removeAttribute('aria-current'));
    activeId = id;
  }
  track.style.width = active.offsetWidth + 'px';
  track.style.transform = `translateX(${active.offsetLeft}px)`;
  nav.classList.add('enhanced');
}
const sections = [...document.querySelectorAll('main > section[id]')];
function updateFromScroll() {
  scrollQueued = false;
  if (scrollAnimation) return;
  const atBottom = window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2;
  const active = atBottom ? sections.at(-1) : [...sections].reverse().find(section => section.getBoundingClientRect().top <= window.innerHeight * .4);
  markActive(active?.id || 'home');
}
const refreshNav = () => {
  const headerHeight = document.querySelector('.header').getBoundingClientRect().height;
  document.documentElement.style.scrollPaddingTop = `${headerHeight + 20}px`;
  markActive(activeId || 'home');
};
refreshNav();
window.addEventListener('resize', refreshNav, { passive: true });
document.fonts?.ready.then(refreshNav);
window.addEventListener('scroll', () => {
  if (!scrollQueued) { scrollQueued = true; requestAnimationFrame(updateFromScroll); }
}, { passive: true });
updateFromScroll();

function stopScroll() {
  if (!scrollAnimation) return;
  cancelAnimationFrame(scrollAnimation.frame);
  scrollAnimation = null;
  updateFromScroll();
}
// Interruptible animation: wheel, touch, and navigation keys keep native control.
window.addEventListener('wheel', stopScroll, { passive: true });
window.addEventListener('touchstart', stopScroll, { passive: true });
window.addEventListener('keydown', event => {
  if (['ArrowUp','ArrowDown','PageUp','PageDown','Home','End',' ','Escape','Tab'].includes(event.key)) stopScroll();
});
window.addEventListener('popstate', stopScroll);
window.addEventListener('resize', stopScroll, { passive: true });
function goToSection(target) {
  stopScroll();
  const startY = window.scrollY;
  const offset = document.querySelector('.header').getBoundingClientRect().height + 20;
  const maximum = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
  const destination = target.id === 'home' ? 0 : Math.min(maximum, Math.max(0, startY + target.getBoundingClientRect().top - offset));
  const time = duration('scroll');
  const complete = () => {
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
    markActive(target.id);
  };
  markActive(target.id);
  if (!time || Math.abs(destination-startY) < 2) {
    window.scrollTo({ top: destination, behavior: 'instant' });
    complete();
    return;
  }
  const state = { frame: 0, start: performance.now(), target, destination };
  scrollAnimation = state;
  function step(now) {
    if (scrollAnimation !== state) return;
    const progress = Math.min(1, (now-state.start)/time);
    const eased = 1-Math.pow(1-progress, 3);
    window.scrollTo({ top: startY+(destination-startY)*eased, behavior: 'instant' });
    if (progress < 1) state.frame = requestAnimationFrame(step);
    else { scrollAnimation = null; complete(); }
  }
  state.frame = requestAnimationFrame(step);
}
document.querySelectorAll('.nav a, .brand, .scroll-link, .back').forEach(link => {
  link.addEventListener('click', event => {
    if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    const target = document.getElementById(link.hash.slice(1));
    if (!target) return;
    event.preventDefault();
    if (location.hash !== link.hash) history.pushState(null, '', link.hash);
    goToSection(target);
  });
});
document.querySelector('[data-language]').addEventListener('change', function() {
  if (!['/', '/zh-tw/'].includes(this.value)) return;
  const url = new URL(this.value, location.origin);
  url.hash = activeId || location.hash;
  location.assign(url.href);
});

const settleDisclosures = [];
document.querySelectorAll('details').forEach(details => {
  const summary = details.querySelector(':scope > summary');
  const content = details.querySelector(':scope > .details-content');
  let animation = null;
  let targetOpen = details.open;
  const settle = () => {
    if (animation) { animation.onfinish = null; animation.cancel(); }
    details.open = targetOpen;
    content.style.overflow = '';
    content.inert = !targetOpen;
    animation = null;
    details.dataset.expanded = String(targetOpen);
  };
  settleDisclosures.push(settle);
  summary.addEventListener('click', event => {
    if (event.target.closest('a, button')) return;
    if (!content.animate) return;
    event.preventDefault();
    // Animate only the content: a hovered summary must remain unclipped.
    const start = details.open ? content.offsetHeight : 0;
    const visibleStyle = getComputedStyle(content);
    const fromOpacity = details.open ? visibleStyle.opacity : '0';
    const fromTransform = details.open ? visibleStyle.transform : 'translateY(8px)';
    targetOpen = !targetOpen;
    if (animation) { animation.onfinish = null; animation.cancel(); }
    details.open = true;
    details.dataset.expanded = String(targetOpen);
    content.style.overflow = 'clip';
    if (!targetOpen && content.contains(document.activeElement)) summary.focus({preventScroll:true});
    content.inert = !targetOpen;
    if (!targetOpen) { content.querySelectorAll('video').forEach(video => video.pause()); resetEmbeds(content); }
    const end = targetOpen ? content.offsetHeight : 0;
    animation = content.animate([
      {height:start+'px', opacity:fromOpacity, transform:fromTransform},
      {height:end+'px', opacity:targetOpen?1:0, transform:targetOpen?'translateY(0)':'translateY(8px)'}
    ], {duration:duration('disclosure'), easing, fill:'both'});
    animation.onfinish = settle;
  });
  details.addEventListener('toggle', () => {
    if (!animation) {
      targetOpen = details.open;
      details.dataset.expanded = String(targetOpen);
      content.inert = !targetOpen;
    }
    if (!details.open) { details.querySelectorAll('video').forEach(video => video.pause()); resetEmbeds(details); }
  });
});
// Reflow must not leave a disclosure with a stale animated height.
window.addEventListener('resize', () => settleDisclosures.forEach(settle => settle()), {passive:true});
document.fonts?.ready.then(() => settleDisclosures.forEach(settle => settle()));
document.addEventListener('visibilitychange', () => {
  if (document.hidden) document.querySelectorAll('video').forEach(video => video.pause());
});
// Prepare only offscreen content before it can enter the viewport. Starting an
// opacity animation on already-visible text causes a visible -> hidden flash.
const revealAnimations = new Map();
if ('IntersectionObserver' in window && Element.prototype.animate) {
  const finishReveal = element => {
    const animation = revealAnimations.get(element);
    if (!animation) return;
    revealObserver.unobserve(element);
    revealAnimations.delete(element);
    animation.onfinish = null;
    animation.cancel(); // Restore the visible CSS state and release the layer.
  };
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const element = entry.target;
      revealObserver.unobserve(element);
      const animation = revealAnimations.get(element);
      if (!animation) return;
      if (element.contains(document.activeElement)) finishReveal(element);
      else animation.play();
    });
  }, {threshold:0, rootMargin:'0px 0px 80px 0px'});
  const revealTargets = '.hero .hello, .hero h1, .hero-bottom, .background, .section-heading, .project, .contact-kicker, .contact h2, .contact-actions, .email-address, .contact-foot, .footer';
  const candidates = [...document.querySelectorAll(revealTargets)].filter(element =>
    element.getBoundingClientRect().top >= window.innerHeight &&
    !element.contains(document.activeElement)
  );
  candidates.forEach(element => {
    const animation = element.animate(
      [{opacity:0, transform:'translateY(18px)'}, {opacity:1, transform:'translateY(0)'}],
      {duration:duration('reveal'), easing, fill:'both'}
    );
    animation.pause();
    animation.currentTime = 0;
    revealAnimations.set(element, animation);
    animation.onfinish = () => finishReveal(element);
    revealObserver.observe(element);
  });
  // Keyboard users and restored pages must never land on hidden content.
  document.addEventListener('focusin', event => {
    revealAnimations.forEach((animation, element) => {
      if (element.contains(event.target)) finishReveal(element);
    });
  });
  window.addEventListener('pageshow', event => {
    if (event.persisted) [...revealAnimations.keys()].forEach(finishReveal);
  });
}
const copy = document.querySelector('[data-copy]');
if (navigator.clipboard?.writeText) {
  copy.hidden = false;
  copy.addEventListener('click', async () => {
    const status = document.querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText('hanssenbudi@gmail.com');
      status.textContent = copy.dataset.copied;
    } catch { status.textContent = copy.dataset.failed; }
  });
}

// Only load YouTube after an explicit click; direct links work without JavaScript.
function resetEmbeds(scope) {
  scope.querySelectorAll('.video-embed').forEach(box => {
    box.querySelector('iframe')?.remove();
    box.querySelector('[data-embed]').hidden = false;
  });
}
document.querySelectorAll('[data-embed]').forEach(link => {
  link.addEventListener('click', event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    const frame = document.createElement('iframe');
    frame.src = link.dataset.embed;
    frame.title = link.dataset.videoTitle;
    frame.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    link.hidden = true;
    link.parentElement.append(frame);
    frame.focus();
  });
});
