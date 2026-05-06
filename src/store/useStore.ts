import { create } from 'zustand';

type Theme = 'dark' | 'light';

interface StoreState {
  theme: Theme;
  toggleTheme: () => void;
  setTheme: (theme: Theme) => void;

  activeSection: string;
  setActiveSection: (section: string) => void;

  sidebarOpen: boolean;
  toggleSidebar: () => void;
  setSidebarOpen: (open: boolean) => void;

  sidebarCollapsed: boolean;
  toggleSidebarCollapsed: () => void;

  commandOpen: boolean;
  setCommandOpen: (open: boolean) => void;

  scrollProgress: number;
  setScrollProgress: (progress: number) => void;
}

const readBool = (key: string, fallback: boolean): boolean => {
  try {
    const v = localStorage.getItem(key);
    if (v === null) return fallback;
    return v === 'true';
  } catch { return fallback; }
};

const writeBool = (key: string, value: boolean) => {
  try { localStorage.setItem(key, String(value)); } catch {}
};

export const useStore = create<StoreState>((set) => ({
  theme: (() => {
    try { return (localStorage.getItem('lujan-theme') as Theme) || 'dark'; }
    catch { return 'dark'; }
  })(),
  toggleTheme: () => set((state) => {
    const next = state.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('lujan-theme', next); } catch {}
    return { theme: next };
  }),
  setTheme: (theme) => {
    try { localStorage.setItem('lujan-theme', theme); } catch {}
    set({ theme });
  },

  activeSection: '',
  setActiveSection: (section) => set({ activeSection: section }),

  sidebarOpen: false,
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setSidebarOpen: (open) => set({ sidebarOpen: open }),

  sidebarCollapsed: readBool('lujan-sidebar-collapsed', false),
  toggleSidebarCollapsed: () => set((state) => {
    const next = !state.sidebarCollapsed;
    writeBool('lujan-sidebar-collapsed', next);
    return { sidebarCollapsed: next };
  }),

  commandOpen: false,
  setCommandOpen: (open) => set({ commandOpen: open }),

  scrollProgress: 0,
  setScrollProgress: (progress) => set({ scrollProgress: progress }),
}));
