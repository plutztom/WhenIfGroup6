import { WhenIfPage } from './app.po';

describe('when-if App', () => {
  let page: WhenIfPage;

  beforeEach(() => {
    page = new WhenIfPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
